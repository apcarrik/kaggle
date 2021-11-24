def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Gender", "instances": 85, "metric_value": 0.8884, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9825, "depth": 2}
		if obj[11]<=19:
			# {"feature": "Income", "instances": 42, "metric_value": 0.9587, "depth": 3}
			if obj[12]>2:
				# {"feature": "Temperature", "instances": 30, "metric_value": 1.0, "depth": 4}
				if obj[2]>30:
					# {"feature": "Education", "instances": 26, "metric_value": 0.9829, "depth": 5}
					if obj[10]>0:
						# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[3]<=1:
							# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[15]>1.0:
								# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[7]<=1:
									return 'False'
								elif obj[7]>1:
									# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]>2:
										return 'False'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[15]<=1.0:
								return 'True'
							else: return 'True'
						elif obj[3]>1:
							return 'True'
						else: return 'True'
					elif obj[10]<=0:
						# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[7]<=5:
							return 'False'
						elif obj[7]>5:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=30:
					return 'True'
				else: return 'True'
			elif obj[12]<=2:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[16]<=2.0:
					return 'True'
				elif obj[16]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]>19:
			return 'False'
		else: return 'False'
	elif obj[6]>0:
		# {"feature": "Restaurantlessthan20", "instances": 40, "metric_value": 0.669, "depth": 2}
		if obj[15]>1.0:
			# {"feature": "Education", "instances": 31, "metric_value": 0.4587, "depth": 3}
			if obj[10]>1:
				return 'True'
			elif obj[10]<=1:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[16]<=1.0:
					# {"feature": "Income", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[12]>3:
						return 'True'
					elif obj[12]<=3:
						# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[8]<=0:
							return 'True'
						elif obj[8]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[16]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]<=1.0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
