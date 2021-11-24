def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Distance", "instances": 70, "metric_value": 0.9787, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coupon", "instances": 63, "metric_value": 0.9468, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Occupation", "instances": 39, "metric_value": 0.8582, "depth": 4}
				if obj[2]>2:
					return 'True'
				elif obj[2]<=2:
					return 'True'
				else: return 'True'
			elif obj[0]>3:
				# {"feature": "Occupation", "instances": 24, "metric_value": 1.0, "depth": 4}
				if obj[2]<=7:
					return 'True'
				elif obj[2]>7:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]<=4:
				return 'False'
			elif obj[2]>4:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[2]>4:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[3]<=1:
				return 'False'
			elif obj[3]>1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=4:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]>2:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					return 'False'
				else: return 'False'
			elif obj[0]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
