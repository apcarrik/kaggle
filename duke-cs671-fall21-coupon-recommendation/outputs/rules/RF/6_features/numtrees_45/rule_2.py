def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[2]>0:
		# {"feature": "Distance", "instances": 12, "metric_value": 1.0, "depth": 2}
		if obj[5]>1:
			# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>1.0:
				return 'False'
			else: return 'False'
		elif obj[5]<=1:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[3]<=14:
			return 'True'
		elif obj[3]>14:
			return 'False'
		else: return 'False'
	else: return 'True'
