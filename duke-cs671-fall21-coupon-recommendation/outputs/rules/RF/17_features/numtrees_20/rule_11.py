def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[13]<=3.0:
		# {"feature": "Maritalstatus", "instances": 48, "metric_value": 0.9183, "depth": 2}
		if obj[7]<=0:
			# {"feature": "Time", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Age", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[6]<=6:
					# {"feature": "Gender", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[16]>1:
							# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[10]>2:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[12]<=1.0:
											return 'True'
										elif obj[12]>1.0:
											return 'False'
										else: return 'False'
									elif obj[0]>2:
										return 'False'
									else: return 'False'
								elif obj[10]<=2:
									return 'False'
								else: return 'False'
							elif obj[3]>3:
								return 'False'
							else: return 'False'
						elif obj[16]<=1:
							# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[8]>0:
								return 'True'
							elif obj[8]<=0:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				elif obj[6]>6:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]<=2:
					return 'True'
				elif obj[0]>2:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>3:
						return 'True'
					elif obj[3]<=3:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]>0:
			# {"feature": "Age", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[6]>2:
				return 'True'
			elif obj[6]<=2:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[16]>1:
					# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[11]<=6:
							return 'True'
						elif obj[11]>6:
							return 'False'
						else: return 'False'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				elif obj[16]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[13]>3.0:
		return 'False'
	else: return 'False'
