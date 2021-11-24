def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]>0:
		# {"feature": "Age", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[6]<=4:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[3]>0:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[10]>6:
					return 'False'
				elif obj[10]<=6:
					# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[12]<=1.0:
						return 'True'
					elif obj[12]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[6]>4:
			return 'True'
		else: return 'True'
	elif obj[7]<=0:
		# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[13]>-1.0:
			return 'True'
		elif obj[13]<=-1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
