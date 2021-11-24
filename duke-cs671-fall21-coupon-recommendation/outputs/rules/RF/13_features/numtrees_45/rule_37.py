def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[10]>0.0:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[2]>1:
			# {"feature": "Age", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[4]>0:
				# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[8]>1.0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[10]<=0.0:
		return 'True'
	else: return 'True'
