def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[15]<=0:
		# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Age", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[6]>2:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=2:
					return 'True'
				elif obj[0]>2:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[7]<=1:
						return 'True'
					elif obj[7]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=2:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[14]>0.0:
					return 'False'
				elif obj[14]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]>2.0:
			return 'True'
		else: return 'True'
	elif obj[15]>0:
		return 'False'
	else: return 'False'
