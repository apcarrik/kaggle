def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Time", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Coupon_validity", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[3]<=2:
						return 'False'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[12]<=1.0:
			return 'False'
		elif obj[12]>1.0:
			return 'True'
		else: return 'True'
	else: return 'False'
