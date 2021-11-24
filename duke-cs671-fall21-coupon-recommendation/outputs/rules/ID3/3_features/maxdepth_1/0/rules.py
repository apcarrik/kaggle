def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4744, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 5889, "metric_value": 0.4676, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 3337, "metric_value": 0.4747, "depth": 3}
			if obj[2]<=13.339599828993485:
				return 'True'
			elif obj[2]>13.339599828993485:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 2552, "metric_value": 0.4568, "depth": 3}
			if obj[2]<=19.03559777229008:
				return 'True'
			elif obj[2]>19.03559777229008:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2258, "metric_value": 0.4882, "depth": 2}
		if obj[2]>2.015213346063521:
			# {"feature": "Education", "instances": 1795, "metric_value": 0.4911, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]<=2.015213346063521:
			# {"feature": "Education", "instances": 463, "metric_value": 0.4395, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
