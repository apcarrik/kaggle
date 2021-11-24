def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9997, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>1:
			# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[3]>1:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
