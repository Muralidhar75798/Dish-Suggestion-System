# search/views.py

from django.shortcuts import render
from .models import Restaurant

def search_view(request):
    query = request.GET.get('q')
    results = []
    recommendations = []
    recommendations_dict = {}
    
    if query:
        # Perform a search query on the 'items' field in Restaurant model
        results = Restaurant.objects.filter(items__icontains=query)
        
        if results:
            all_items = ','.join([restaurant.items for restaurant in results])
            print(all_items)
            all_items_list = [item.strip() for item in set(all_items.split(','))]
            print(all_items_list)
            
            # Filter recommendations based on the query
            recommendations = [item for item in all_items_list if query.lower() in item.lower()]
            print(results)

            
            for restaurant in results:
                print(vars(restaurant)) 
                matched_items = [item.strip() for item in restaurant.items.split(',') if query.lower() in item.lower()]
                if matched_items:
                    aggregate_rating = restaurant.aggregate_rating
                    if aggregate_rating is None:
                        aggregate_rating = float('-inf')  # Use negative infinity for no rating

                    recommendations_dict[restaurant.name] = {
                        'items': matched_items,
                        'aggregate_rating': aggregate_rating  # Ensure it's float for sorting
                    }
            
            # Sort recommendations by aggregate rating, handling None values
            sorted_recommendations = sorted(
                recommendations_dict.items(),
                key=lambda x: (x[1]['aggregate_rating'] is not None, x[1]['aggregate_rating']),
                reverse=True  # Sort by rating descending
            )
            
            # Convert back to a dictionary with items and ratings
            recommendations_dict = {
                k: {'items': v['items'], 'aggregate_rating': v['aggregate_rating'] if v['aggregate_rating'] != float('-inf') else None}
                for k, v in sorted_recommendations
            }

            print(f"Recommendations dict: {recommendations_dict}")
    
    #return render(request, 'search/search.html', {'results': results, 'recommendations': recommendations, 'query': query})
    return render(request, 'search/search.html', {'results': results, 'recommendations_dict':recommendations_dict, 'query': query})
