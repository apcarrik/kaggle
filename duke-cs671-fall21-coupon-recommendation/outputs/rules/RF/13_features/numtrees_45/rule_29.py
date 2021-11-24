def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[7]<=6:
			# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[4]<=4:
				# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[8]<=0.0:
					# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[8]>0.0:
					return 'True'
				else: return 'True'
			elif obj[4]>4:
				return 'False'
			else: return 'False'
		elif obj[7]>6:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[4]<=6:
			return 'False'
		elif obj[4]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
