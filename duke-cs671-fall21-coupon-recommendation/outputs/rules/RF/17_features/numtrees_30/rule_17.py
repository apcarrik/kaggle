def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 2}
		if obj[16]<=1:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[12]<=0.0:
				return 'True'
			elif obj[12]>0.0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>2:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]>0:
						return 'False'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[16]>1:
			# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[6]<=5:
				return 'False'
			elif obj[6]>5:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
