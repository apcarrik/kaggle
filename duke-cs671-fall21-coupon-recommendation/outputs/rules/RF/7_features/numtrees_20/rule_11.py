def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[1]>0:
		# {"feature": "Passanger", "instances": 48, "metric_value": 0.9887, "depth": 2}
		if obj[0]>0:
			# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.9968, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Education", "instances": 42, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Distance", "instances": 28, "metric_value": 0.9852, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Direction_same", "instances": 26, "metric_value": 0.9957, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 7}
							if obj[3]<=11:
								return 'False'
							elif obj[3]>11:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]<=11:
								return 'True'
							elif obj[3]>11:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[3]>5:
						return 'False'
					elif obj[3]<=5:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
