def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Time", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Education", "instances": 41, "metric_value": 0.9996, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Passanger", "instances": 33, "metric_value": 0.9457, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Bar", "instances": 21, "metric_value": 0.9587, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[8]>1:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]>0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						elif obj[8]<=1:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[6]>-1.0:
								# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]<=-1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=0.0:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>1.0:
								return 'False'
							elif obj[6]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[4]>7:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
