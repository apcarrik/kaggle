def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[12]>1:
		# {"feature": "Passanger", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[11]>3:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[17]<=0:
					return 'False'
				elif obj[17]>0:
					return 'True'
				else: return 'True'
			elif obj[11]<=3:
				# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]>55:
					return 'True'
				elif obj[2]<=55:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[12]<=1:
		return 'True'
	else: return 'True'
