def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>1:
		# {"feature": "Age", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[4]>0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[6]>1:
				# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>2:
							return 'False'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
