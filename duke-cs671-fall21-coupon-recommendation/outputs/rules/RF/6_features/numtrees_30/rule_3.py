def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=11:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[3]>11:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>2:
					return 'True'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
