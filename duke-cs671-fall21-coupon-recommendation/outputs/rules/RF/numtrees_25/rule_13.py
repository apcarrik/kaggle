def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 41, "metric_value": 0.9789, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 2}
		if obj[5]>1:
			# {"feature": "Carryaway", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[16]>1.0:
				# {"feature": "Income", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[13]>2:
					# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[8]<=5:
						return 'True'
					elif obj[8]>5:
						return 'False'
					else: return 'False'
				elif obj[13]<=2:
					# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[9]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[16]<=1.0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=3:
					return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=1:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[12]<=9:
				return 'False'
			elif obj[12]>9:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>2:
		return 'True'
	else: return 'True'
