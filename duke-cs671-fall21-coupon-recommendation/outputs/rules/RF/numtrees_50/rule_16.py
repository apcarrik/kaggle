def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Occupation", "instances": 20, "metric_value": 1.0, "depth": 1}
	if obj[12]<=14:
		# {"feature": "Restaurantlessthan20", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[17]<=2.0:
			# {"feature": "Driving_to", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[0]>0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=0:
						return 'True'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[17]>2.0:
			return 'False'
		else: return 'False'
	elif obj[12]>14:
		return 'True'
	else: return 'True'
