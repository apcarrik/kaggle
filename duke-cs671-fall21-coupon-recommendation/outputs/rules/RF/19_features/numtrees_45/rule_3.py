def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Income", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[12]<=6:
			# {"feature": "Age", "instances": 15, "metric_value": 0.3534, "depth": 3}
			if obj[7]<=4:
				return 'False'
			elif obj[7]>4:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]>6:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
