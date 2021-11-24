def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 4}
				if obj[3]<=6:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>6:
					return 'True'
				else: return 'True'
			elif obj[4]>2.0:
				return 'False'
			else: return 'False'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[3]<=10:
			return 'False'
		elif obj[3]>10:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
