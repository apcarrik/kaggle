def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 38, "metric_value": 0.9819, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 30, "metric_value": 1.0, "depth": 3}
			if obj[4]<=17:
				# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.9911, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Education", "instances": 25, "metric_value": 0.9988, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Distance", "instances": 24, "metric_value": 1.0, "depth": 6}
						if obj[8]<=1:
							# {"feature": "Bar", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]<=0.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]>1:
							# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[1]>0:
								# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[5]>1.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[5]<=1.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[6]>2.0:
					return 'True'
				else: return 'True'
			elif obj[4]>17:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[7]<=0:
				return 'False'
			elif obj[7]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[4]>0:
			return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
