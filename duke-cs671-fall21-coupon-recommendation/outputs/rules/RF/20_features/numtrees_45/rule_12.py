def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Driving_to", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=0:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[12]<=8:
			return 'True'
		elif obj[12]>8:
			# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[6]<=0:
				return 'True'
			elif obj[6]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>0:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[12]<=6:
			return 'False'
		elif obj[12]>6:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
