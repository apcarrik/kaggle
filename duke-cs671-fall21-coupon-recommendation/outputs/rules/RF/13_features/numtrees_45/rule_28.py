def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]<=9:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[8]>-1.0:
			# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[12]>1:
				# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>2:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=1.0:
								return 'True'
							elif obj[10]>1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[12]<=1:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[9]<=3.0:
					return 'True'
				elif obj[9]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=-1.0:
			return 'False'
		else: return 'False'
	elif obj[7]>9:
		# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=1:
				return 'False'
			elif obj[2]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
