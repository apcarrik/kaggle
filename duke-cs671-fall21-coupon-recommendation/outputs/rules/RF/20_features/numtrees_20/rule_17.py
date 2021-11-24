def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[5]>0:
		# {"feature": "Coupon_validity", "instances": 48, "metric_value": 0.9887, "depth": 2}
		if obj[6]>0:
			# {"feature": "Children", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Income", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[13]<=5:
					return 'False'
				elif obj[13]>5:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=2:
							return 'False'
						elif obj[8]>2:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]>0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[12]>1:
					# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[13]>1:
						return 'True'
					elif obj[13]<=1:
						return 'False'
					else: return 'False'
				elif obj[12]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]<=0:
			# {"feature": "Time", "instances": 24, "metric_value": 0.8113, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Bar", "instances": 22, "metric_value": 0.684, "depth": 4}
				if obj[14]<=0.0:
					# {"feature": "Weather", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[8]<=2:
							return 'True'
						elif obj[8]>2:
							# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[9]<=0:
								return 'True'
							elif obj[9]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				elif obj[14]>0.0:
					return 'True'
				else: return 'True'
			elif obj[4]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=0:
		return 'False'
	else: return 'False'
