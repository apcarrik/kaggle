def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[10]<=7:
		# {"feature": "Bar", "instances": 47, "metric_value": 0.9918, "depth": 2}
		if obj[11]<=2.0:
			# {"feature": "Passanger", "instances": 40, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				# {"feature": "Weather", "instances": 38, "metric_value": 0.998, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Age", "instances": 33, "metric_value": 0.9834, "depth": 5}
					if obj[6]<=6:
						# {"feature": "Coupon_validity", "instances": 30, "metric_value": 0.9968, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 7}
							if obj[3]>0:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[12]<=3.0:
									# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[9]<=12:
										return 'True'
									elif obj[9]>12:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2]>2:
											return 'True'
										elif obj[2]<=2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]>3.0:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]<=0:
									return 'False'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>0:
							# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[3]>2:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[2]>0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=2:
											return 'True'
										elif obj[8]>2:
											return 'False'
										else: return 'False'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							elif obj[3]<=2:
								# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[2]>2:
									# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[2]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>6:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]>0:
						return 'False'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[11]>2.0:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[3]<=3:
				return 'True'
			elif obj[3]>3:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[10]>7:
		return 'True'
	else: return 'True'
