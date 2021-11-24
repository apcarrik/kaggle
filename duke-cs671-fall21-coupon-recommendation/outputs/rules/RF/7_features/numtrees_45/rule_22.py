def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[3]<=14:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[0]<=2:
					return 'True'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>14:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=3:
					return 'False'
				elif obj[3]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
