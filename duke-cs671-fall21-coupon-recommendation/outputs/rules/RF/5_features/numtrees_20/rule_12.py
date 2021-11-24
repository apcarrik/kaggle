def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 40, "metric_value": 0.9982, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.9868, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Coupon", "instances": 35, "metric_value": 0.971, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Education", "instances": 22, "metric_value": 0.9024, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[0]>3:
					# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[1]<=4:
						return 'False'
					elif obj[1]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>2.0:
				return 'False'
			else: return 'False'
		elif obj[4]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
