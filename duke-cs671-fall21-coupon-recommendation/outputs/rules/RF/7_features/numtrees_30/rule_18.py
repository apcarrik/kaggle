def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.9544, "depth": 2}
		if obj[3]<=6:
			# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Passanger", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=1.0:
								return 'True'
							elif obj[4]>1.0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[3]>6:
			# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Education", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
