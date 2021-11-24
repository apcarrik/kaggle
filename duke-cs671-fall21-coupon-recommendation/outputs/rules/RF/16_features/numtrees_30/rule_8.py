def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[9]<=10:
		# {"feature": "Direction_same", "instances": 32, "metric_value": 0.9284, "depth": 2}
		if obj[14]<=0:
			# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.8631, "depth": 3}
			if obj[12]<=3.0:
				# {"feature": "Time", "instances": 27, "metric_value": 0.8256, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 5}
					if obj[3]>0:
						# {"feature": "Age", "instances": 21, "metric_value": 0.7919, "depth": 6}
						if obj[6]<=4:
							# {"feature": "Gender", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[11]>0.0:
										return 'True'
									elif obj[11]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]>4:
							# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[10]<=4:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=0.0:
									# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=0:
												return 'False'
											elif obj[7]>0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[4]>0:
										return 'True'
									else: return 'True'
								elif obj[11]>0.0:
									return 'True'
								else: return 'True'
							elif obj[10]>4:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[12]>3.0:
				return 'False'
			else: return 'False'
		elif obj[14]>0:
			# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[9]>10:
		return 'False'
	else: return 'False'
