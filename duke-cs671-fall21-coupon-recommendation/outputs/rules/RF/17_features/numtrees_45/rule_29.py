def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=9:
		# {"feature": "Bar", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[12]>0.0:
			# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[12]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[10]>9:
		return 'False'
	else: return 'False'
