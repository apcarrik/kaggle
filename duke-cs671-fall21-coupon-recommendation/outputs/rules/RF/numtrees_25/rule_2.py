def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Income", "instances": 41, "metric_value": 0.965, "depth": 1}
	if obj[13]<=6:
		# {"feature": "Driving_to", "instances": 37, "metric_value": 0.909, "depth": 2}
		if obj[0]<=0:
			# {"feature": "Passanger", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[1]>2:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[5]>0:
					# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[8]>0:
						return 'True'
					elif obj[8]<=0:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		elif obj[0]>0:
			# {"feature": "Education", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[11]>1:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[8]<=3:
						return 'False'
					elif obj[8]>3:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[11]<=1:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[13]>6:
		return 'False'
	else: return 'False'
