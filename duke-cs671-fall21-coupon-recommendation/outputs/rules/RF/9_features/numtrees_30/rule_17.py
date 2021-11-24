def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]<=2.0:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.9968, "depth": 2}
		if obj[2]>3:
			# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[4]>5:
						return 'False'
					elif obj[4]<=5:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>5:
						return 'True'
					elif obj[4]<=5:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]<=3:
			# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[1]>1:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>1:
						# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				elif obj[4]>7:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]>2.0:
		return 'True'
	else: return 'True'
