def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Time", "instances": 29, "metric_value": 0.8936, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.9427, "depth": 3}
			if obj[7]<=15:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[4]>1:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Children", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2]<=2:
										return 'False'
									elif obj[2]>2:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>1.0:
							return 'True'
						else: return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[10]>1.0:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>2:
							return 'False'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[7]>15:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[6]>3:
		return 'True'
	else: return 'True'
