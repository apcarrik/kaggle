def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[4]<=20:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.9932, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[6]>-1.0:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[5]<=3.0:
						# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>1:
										return 'True'
									elif obj[8]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[3]>0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[5]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[6]<=-1.0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[6]<=1.0:
				return 'True'
			elif obj[6]>1.0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=2:
						return 'False'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[4]>20:
		return 'False'
	else: return 'False'
