def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon_validity", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.8113, "depth": 2}
		if obj[4]>0:
			# {"feature": "Age", "instances": 30, "metric_value": 0.7219, "depth": 3}
			if obj[7]<=4:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 4}
				if obj[11]<=20:
					# {"feature": "Income", "instances": 21, "metric_value": 0.7025, "depth": 5}
					if obj[12]>4:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[3]<=1:
								# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[1]<=1:
									return 'True'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							elif obj[3]>1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[12]<=4:
						return 'True'
					else: return 'True'
				elif obj[11]>20:
					return 'False'
				else: return 'False'
			elif obj[7]>4:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[5]>0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[10]>0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[11]>1:
				return 'False'
			elif obj[11]<=1:
				return 'True'
			else: return 'True'
		elif obj[10]<=0:
			# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[14]<=2.0:
					return 'True'
				elif obj[14]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
