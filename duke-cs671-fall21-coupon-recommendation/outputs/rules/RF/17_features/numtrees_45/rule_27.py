def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[15]<=0:
		# {"feature": "Bar", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Passanger", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[11]<=5:
					return 'False'
				elif obj[11]>5:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>2:
						return 'True'
					elif obj[3]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[10]>5:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]>1:
						return 'False'
					elif obj[7]<=1:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[10]<=5:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[12]>1.0:
			return 'True'
		else: return 'True'
	elif obj[15]>0:
		return 'True'
	else: return 'True'
