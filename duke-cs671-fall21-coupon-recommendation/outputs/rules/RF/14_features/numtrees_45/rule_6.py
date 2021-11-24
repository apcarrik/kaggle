def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[7]<=21:
			# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[6]>1:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=2:
						return 'True'
					elif obj[8]>2:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]<=1:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[11]>0.0:
					return 'True'
				elif obj[11]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]>21:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
