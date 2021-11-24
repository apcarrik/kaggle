def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[2]<=11:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[2]>11:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=7:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]>7:
					return 'False'
				else: return 'False'
			elif obj[3]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
