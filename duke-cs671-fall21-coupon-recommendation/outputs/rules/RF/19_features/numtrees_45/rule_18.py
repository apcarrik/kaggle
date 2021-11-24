def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]>0:
		# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		elif obj[14]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[10]<=0:
		# {"feature": "Income", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[12]<=4:
			return 'True'
		elif obj[12]>4:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]<=2:
				return 'False'
			elif obj[3]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
