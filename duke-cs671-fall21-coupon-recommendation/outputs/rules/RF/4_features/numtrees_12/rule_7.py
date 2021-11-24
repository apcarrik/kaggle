def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[2]>2:
		# {"feature": "Coupon", "instances": 63, "metric_value": 0.9852, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 53, "metric_value": 0.9977, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 38, "metric_value": 0.998, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]<=0:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=2:
		# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[3]>1:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
