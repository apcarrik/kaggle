def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9341, "depth": 1}
	if obj[18]<=1.0:
		# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[15]<=1.0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Driving_to", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>55:
						return 'False'
					elif obj[3]<=55:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>3:
				return 'True'
			else: return 'True'
		elif obj[15]>1.0:
			return 'False'
		else: return 'False'
	elif obj[18]>1.0:
		# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[4]>0:
			return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
