def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[8]<=6:
		# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coffeehouse", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[10]<=3.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[7]<=11:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[7]>11:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>3.0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[8]>6:
		return 'True'
	else: return 'True'
