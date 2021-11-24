def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[11]>5:
			# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[12]>2:
				# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[15]<=2.0:
					return 'True'
				elif obj[15]>2.0:
					return 'False'
				else: return 'False'
			elif obj[12]<=2:
				return 'False'
			else: return 'False'
		elif obj[11]<=5:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'
