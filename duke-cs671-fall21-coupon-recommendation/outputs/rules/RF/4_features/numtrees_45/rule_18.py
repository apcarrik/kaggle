def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[2]>5:
		# {"feature": "Education", "instances": 16, "metric_value": 0.3373, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]>1:
				return 'False'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=5:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
