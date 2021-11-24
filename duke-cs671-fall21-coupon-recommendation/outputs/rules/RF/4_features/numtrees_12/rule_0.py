def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 52, "metric_value": 0.9904, "depth": 2}
		if obj[2]<=8:
			# {"feature": "Distance", "instances": 30, "metric_value": 0.9968, "depth": 3}
			if obj[3]>1:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>8:
			# {"feature": "Coupon", "instances": 22, "metric_value": 0.9024, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Distance", "instances": 33, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.8691, "depth": 3}
			if obj[2]<=10:
				# {"feature": "Coupon", "instances": 26, "metric_value": 0.7793, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					return 'True'
				else: return 'True'
			elif obj[2]>10:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[0]>2:
					return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
