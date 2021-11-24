def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[6]>1:
		# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Passanger", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=7:
						return 'False'
					elif obj[3]>7:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>2:
							return 'False'
						elif obj[2]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=0.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=1:
		# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
