def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[13]>0.0:
					return 'True'
				elif obj[13]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
