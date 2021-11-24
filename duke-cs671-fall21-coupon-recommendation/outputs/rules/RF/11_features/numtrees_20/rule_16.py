def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[5]<=14:
		# {"feature": "Direction_same", "instances": 44, "metric_value": 0.994, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.9923, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[10]<=2:
								# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[3]>0:
									# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[6]<=0.0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[0]>1:
												return 'False'
											elif obj[0]<=1:
												return 'True'
											else: return 'True'
										elif obj[6]>0.0:
											return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[10]>2:
								return 'True'
							else: return 'True'
						elif obj[4]>2:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[7]>2.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[9]>0:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]>14:
		return 'False'
	else: return 'False'
