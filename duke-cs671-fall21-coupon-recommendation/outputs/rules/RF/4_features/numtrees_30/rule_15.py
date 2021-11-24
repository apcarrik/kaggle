def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]>5:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[3]>1:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=5:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
