def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[4]>0:
		# {"feature": "Occupation", "instances": 72, "metric_value": 0.9726, "depth": 2}
		if obj[11]<=12:
			# {"feature": "Education", "instances": 56, "metric_value": 0.9241, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Coupon_validity", "instances": 46, "metric_value": 0.8281, "depth": 4}
				if obj[5]>0:
					# {"feature": "Time", "instances": 28, "metric_value": 0.9666, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Income", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[12]<=5:
							# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[12]>5:
							# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[7]>2:
								return 'True'
							elif obj[7]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>2:
						# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[8]<=1:
							return 'True'
						elif obj[8]>1:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=0:
					# {"feature": "Income", "instances": 18, "metric_value": 0.3095, "depth": 5}
					if obj[12]<=7:
						return 'True'
					elif obj[12]>7:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>2:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[18]>1:
					return 'False'
				elif obj[18]<=1:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[11]>12:
			# {"feature": "Temperature", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[2]>55:
				# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[15]>-1.0:
					return 'False'
				elif obj[15]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=55:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]<=2:
						return 'False'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=0:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[11]<=10:
			# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[3]<=3:
				return 'False'
			elif obj[3]>3:
				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]>10:
			return 'True'
		else: return 'True'
	else: return 'False'
