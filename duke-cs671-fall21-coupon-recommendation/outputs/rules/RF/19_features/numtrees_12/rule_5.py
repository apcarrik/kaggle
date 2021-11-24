def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[18]>1:
		# {"feature": "Time", "instances": 56, "metric_value": 0.9666, "depth": 2}
		if obj[3]>0:
			# {"feature": "Coupon", "instances": 46, "metric_value": 0.9109, "depth": 3}
			if obj[4]>2:
				# {"feature": "Coupon_validity", "instances": 25, "metric_value": 0.9988, "depth": 4}
				if obj[5]>0:
					# {"feature": "Occupation", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[11]>1:
						# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 6}
						if obj[16]>0.0:
							# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 7}
							if obj[7]>1:
								return 'False'
							elif obj[7]<=1:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[16]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[11]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[10]<=2:
						return 'True'
					elif obj[10]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=2:
				# {"feature": "Occupation", "instances": 21, "metric_value": 0.5917, "depth": 4}
				if obj[11]<=10:
					return 'False'
				elif obj[11]>10:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[14]<=1.0:
						return 'False'
					elif obj[14]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[3]<=0:
			# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[8]<=1:
				return 'True'
			elif obj[8]>1:
				# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=0:
					return 'False'
				elif obj[6]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[18]<=1:
		# {"feature": "Children", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[10]<=1:
				# {"feature": "Temperature", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[2]>55:
					return 'True'
				elif obj[2]<=55:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>1:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[0]>0:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[11]>1:
						return 'False'
					elif obj[11]<=1:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[7]<=1:
							return 'False'
						elif obj[7]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>0:
			return 'True'
		else: return 'True'
	else: return 'True'
